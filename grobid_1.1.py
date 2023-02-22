from grobid.client import GrobidClient

client = GrobidClient()
client.process("processFulltextDocument", "/mnt/data/covid/pdfs", n=20)