import re
import sys
import json
import subprocess
import traceback
import xml.etree.ElementTree as ET

def main(**args):
  manifest_file = args['manifest_file']
  mode = args['mode']
  out_dir = args['output_dir']
  log_file_path = args['log_file']
  if mode != 'pdf' and mode != 'src':
    print('mode should be "pdf" or "src"')

  def get_file(fname, out_dir):
    cmd = ['s3cmd', 'get', '--requester-pays',
           's3://arxiv/%s' % fname, './%s' % out_dir]
    print(' '.join(cmd))
    subprocess.call(' '.join(cmd), shell=True)

  log_file = open(log_file_path, 'a')
  try:
    for event, elem in ET.iterparse(manifest_file):
      if event == 'end':
        if elem.tag == 'filename':
          fname = elem.text
          get_file(fname, out_dir='%s/%s/' % (out_dir, mode))
          log_file.write(fname + '\n')
  except:
    traceback.print_exc()

  print('Finished')


if __name__ == '__main__':
  from argparse import ArgumentParser
  ap = ArgumentParser()
  ap.add_argument('--manifest_file', '-m', type=str, help='The manifest file for downloading from arxiv. Obtain it from s3://arxiv/pdf/arXiv_pdf_manifest.xml using `s3cmd get --add-header="x-amz-request-payer: requester" s3://arxiv/pdf/arXiv_pdf_manifest.xml`', required=True)
  ap.add_argument('--output_dir', '-o', type=str, default='data', help='the output directory')
  ap.add_argument('--mode', type=str, default='src', choices=set(('pdf', 'src')),
                  help='can be "pdf" or "src"')
  ap.add_argument('--log_file', default='processed.txt', help='a file that logs the processed txt files')
  args = ap.parse_args()
  main(**vars(args))
