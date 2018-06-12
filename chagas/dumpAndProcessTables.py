# prerequisite https://github.com/brianb/mdbtools
import argparse
import sys, subprocess, os
import pandas as pd



def get_args():
    parser = argparse.ArgumentParser(description=' full pipeline for dump and preprocess ChagasDB writed in Access')
    parser.add_argument('-i','--input_db',required=True)
    parser.add_argument('-o','--opath',required=True)  
    # parse args
    args = parser.parse_args()
    return args


def DumpDb(imput_db,dump_path):
#    ..... aca hay que bajar este codigo ---> #python ./AccessDump.py $1 | sqlite3 $1.sqlite

    # AccessDump.py
    # A simple script to dump the contents of a Microsoft Access Database.
    # It depends upon the mdbtools suite:
    #   http://sourceforge.net/projects/mdbtools/

    # Dump the schema for the DB
    subprocess.call(["mdb-schema", imput_db, "mysql"])

    # Get the list of table names with "mdb-tables"
    table_names = subprocess.Popen(["mdb-tables", "-1", imput_db],
                                stdout=subprocess.PIPE).communicate()[0]
    tables = table_names.splitlines()

    print "BEGIN;" # start a transaction, speeds things up when importing
    sys.stdout.flush() # te permite ver el print anterior inmediatamente en la consola

    # Dump each table as a CSV file using "mdb-export",
    # converting " " in table names to "_" for the CSV filenames.
    with open(dump_path + 'Chagas.sql','wb') as f:
        for table in tables:
            if table != '':
                #subprocess.call(["mdb-export", "-I", "mysql", imput_db, table])
                table_content = subprocess.Popen(["mdb-export", "-I", "mysql", imput_db, table],stdout=subprocess.PIPE).communicate()[0]                
            f.write(table_content)
    f.close()

    for table in tables:
        ffile = dump_path+table+'.csv'
        with open(ffile,'wb') as f:
            if table != '':
                tc = subprocess.Popen(['mdb-export', input_db, table],stdout=subprocess.PIPE).communicate()[0]
            f.write(tc)
        f.close()
    

            
    print "COMMIT;" # end the transaction
    sys.stdout.flush()


    #os.system('for x in `mdb-tables -1 %s`; do mdb-export %s $x >> %s.$x.csv ; done'%(input_db,input_db,dump_path))
    #os.system('mv %s.sqlite %s'%(input_db,dump_path))

# create output directories    
def create_output_dirs(opath):
    if not os.path.exists(opath):
        os.mkdir(opath)

    dump_path = opath+'dump/'
    proc_path = opath + 'processed-tables/'

    if not os.path.exists(dump_path):
        os.mkdir(dump_path)    
    if not os.path.exists(proc_path):
        os.mkdir(proc_path)
    return dump_path,proc_path
    
def JoinSerotipeTables(dump_path):
    sero1 = dump_path+'Serologia.csv'
    sero2 = dump_path+'Serolog\xc3\xada2.csv'
    s1 = pd.read_csv(sero1)
    s1.set_index('HistoriaClinica',inplace= True)

    s2 = pd.read_csv(sero2)
    s2.set_index('HistoriaClinica',inplace=True)

    serototal = pd.concat([s1,s2],axis = 1)

    serototal.to_csv(dump_path+'Serologias.csv')
    subprocess.call(['rm',sero1])
    subprocess.call(['rm',sero2])
    

if __name__ == '__main__' : 
    args = get_args()
    input_db, opath = args.input_db, args.opath

    dump_path,proc_path =  create_output_dirs(opath)
    
    #this function dump the entire db in sql script and tablee by table in csv format
    #the output is downstream opath, in dump folder
    DumpDb(input_db,dump_path)    
    

    #esto reemplaza el scrppython join_sertotipe_tables.py 
    JoinSerotipeTables(dump_path)


    #python transformDB.py # este file llama a parse_raw_data.py que es el que tiene la papota, cualquier ascepcion de procesamiento debe modificarse en 'parse_raw_data.py'
