from invenio_records_resources.services.files.processors import FileProcessor
from invenio_records_resources.services.uow import UnitOfWork, RecordCommitOp
from oarepo_runtime.datastreams.utils import get_record_service_for_record

import logging

tpr_log = logging.getLogger("extract-tpr-parameters-processor")


class ExtractTPRParametersProcessor(FileProcessor):

    def can_process(self, file_record):
        return self.file_extension(file_record) == '.tpr'

    def process(self, file_record):
        """Process a file."""
        try:
            tpr_log.info(f"Extracting text from PDF file {file_record.key}")
            with file_record.open_stream("rb") as fp:
                data = fp.read()
                # TODO: add your processor here

                record = file_record.record

                simulations = record['metadata'].setdefault('simulations', [])
                for sim in simulations:
                    if sim.get('key') == file_record.key:
                        found_simulation = sim
                        break
                else:
                    found_simulation = {'key': file_record.key}
                    simulations.append(found_simulation)
                # TODO: fill in found_simulation metadata here

                with UnitOfWork() as uow:
                    record_service = get_record_service_for_record(record)
                    if record_service:
                        indexer = record_service.indexer
                        uow.register(RecordCommitOp(record, indexer, index_refresh=True))
                        uow.commit()
        except Exception as e:
            record_id = file_record.record.get('id') or file_record.record.id
            tpr_log.exception(f"Error extracting text from pdf file {file_record.key} on record {record_id}: {e}")

