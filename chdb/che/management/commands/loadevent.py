import csv
from django.core.management.base import BaseCommand, CommandError
from django.db import DatabaseError, transaction
from che.models import Disk, Event, ModelAtmosphere, ModelGrid, ModelInteraction, Particle


class Command(BaseCommand):
    help = 'Loads event data from CSV files.'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        self.disk_id_by_name = {
            disk.name: disk.id
                for disk in Disk.objects.all()
        }
        self.model_atmosphere_id_by_code = {
            model_atmosphere.code: model_atmosphere.id
                for model_atmosphere in ModelAtmosphere.objects.all()
        }
        self.model_grid_id_by_name = {
            model_grid.name: model_grid.id
                for model_grid in ModelGrid.objects.all()
        }
        self.model_interaction_id_by_name = {
            model_interaction.name: model_interaction.id
                for model_interaction in ModelInteraction.objects.all()
        }
        self.particle_id_by_code = {
            particle.code: particle.id
                for particle in Particle.objects.all()
        }
        for filename in options['file']:
            self.stdout.write(f'File: {filename}')
            if self.load_file(filename):
                self.stdout.write('Ok')
        self.stdout.write('Done')

    def load_file(self, filename):
        ok = False
        line = None
        try:
            skip = set()
            with open(filename, 'r', newline='') as file:
                with transaction.atomic():
                    reader = csv.DictReader(file)
                    for prop in reader.fieldnames:
                        if prop != 'file' and not hasattr(Event, prop):
                            skip.add(prop)
                    if skip:
                        self.stderr.write(f'''Skipped columns: {(', ').join(sorted(skip))}''')
                    for row in reader:
                        line = reader.line_num
                        if 'file' in row:
                            row.pop('file');
                        if 'disk' in row:
                            name = row.pop('disk')
                            if name not in self.disk_id_by_name:
                                raise ValueError(f'Disk name = {name}')
                            row['disk_id'] = self.disk_id_by_name[name]
                        if 'model_atmosphere' in row:
                            code = int(row.pop('model_atmosphere'))
                            if code not in self.model_atmosphere_id_by_code:
                                raise ValueError(f'ModelAtmosphere code = {code}')
                            row['model_atmosphere_id'] = self.model_atmosphere_id_by_code[code]
                        if 'model_grid' in row:
                            name = row.pop('model_grid')
                            if name not in self.model_grid_id_by_name:
                                raise ValueError(f'ModelGrid name = {name}')
                            row['model_grid_id'] = self.model_grid_id_by_name[name]
                        if 'model_interaction' in row:
                            name = row.pop('model_interaction')
                            if name not in self.model_interaction_id_by_name:
                                raise ValueError(f'ModelInteraction name = {name}')
                            row['model_interaction_id'] = self.model_interaction_id_by_name[name]
                        if 'particle' in row:
                            code = int(row.pop('particle'))
                            if code not in self.particle_id_by_code:
                                raise ValueError(f'Particle code = {code}')
                            row['particle_id'] = self.particle_id_by_code[code]
                        for prop in skip:
                            row.pop(prop)
                        event = Event(**row)
                        event.save()
        except DatabaseError as err:
            self.stderr.write(f'Database error: {err}')
        except ValueError as err:
            self.stderr.write(f'Value error: {err}')
        except Exception as err:
            self.stderr.write(f'Error: {err}')
        else:
            ok = True
        finally:
            if not ok and line is not None:
                self.stderr.write(f'File: {filename}, line {line}')
        return ok
