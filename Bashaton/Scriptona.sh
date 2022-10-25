  292  git clone https://github.com/AJVelezRueda/Scriptona.git

  293  cd Scriptona/

  294  ./welcome.sh 

  295  cd paso_2

  296  cat instrucciones.txt

  297  cd ..

  298  cd paso_5

  299  cat instrucciones.txt 

  300  head -n 2 instrucciones.txt 

  301  cd paso_10

  302  cd ..

  303  cd paso_10

  304  cat instrucciones.txt 

  305  wget https://www.gnu.org/licenses/gpl-3.0.txt

  306  cat gpl-3.0.txt | grep freedom | wc -l

  307  cd ..

  308  cd paso_8

  309  wget https://www.rcsb.org/fasta/entry/7PND

  310  cat 7PND | grep K

  311  cat 7PND | grep K | wc -m

  312  cat 7PND | grep K | wc -w

  313  grep -i 'K' 7PND 

  314  grep -ic 'K' 7PND 

  315  grep -o 'K' 7PND 

  316  grep -o 'K' 7PND | wc -l

  317  cd ..

  318  cd paso_24

  319  cat instrucciones.txt 

  320  wget https://www.alphafold.ebi.ac.uk/entry/F4HVG8

  321  ls

  322  ls -ltah

  323  cd ..

  324  cd paso_7

  325  cat instrucciones.txt 

  326  ls

  327  cat sequences.fasta sequences_II.fasta | grep 'Homo sapines' | wc -l

  328  cd ..

  329  cd paso_0

  330  cat sequences.fasta sequences_II.fasta | grep 'Homo sapines' 

  331  cd paso_7

  332  cat sequences.fasta sequences_II.fasta | grep 'Homo sapines' 

  333  cat sequences.fasta sequences_II.fasta | grep 'Homo sapines' | wc -w

  334  cat sequences.fasta sequences_II.fasta | grep 'Homo sapiens' | wc -w

  335  cd ..

  336  cd paso_18

  337  cat sequences.fasta sequences_II.fasta | grep 'Homo sapiens' | wc -l

  338  cd paso_7

  339  cat sequences.fasta sequences_II.fasta | grep 'Homo sapiens' | wc -l

  340  cd ..

  341  cd paso_9

  342  cat instrucciones.txt 

  343  ls

  344  cat *.txt

  345  cat arch_III.txt

  346  cat *.txt

  347  cat *.txt | cut -f 2-2

  348  cut -f 2-2 | cat *.txt

  349  cut -f 2-2 *.txt

  350  cut -f 2-2 -d":" --output-delimiter="; " *.txt

  351  cut -f 2-2 -d":" --output-delimiter="; " instrucciones.txt 

  352  cut -d ',' -f 2,2 instrucciones.txt 

  353  cut -d ',' -f 2,2 arch_III.txt

  354  cut -d ',' -f 2,2 arch_II.txt

  355  cut -d ',' -f 2,2 | cat arch_III.txt arch_II.txt

  356  cut -d ',' -f 2,2 (cat arch_III.txt arch_II.txt)

  357  ARCHIVOS=cat arch_III.txt arch_II.txt cut -d ',' -f 2,2 $ARCHIVOS 

  358  cat arch_III.txt arch_II.txt | cut -d ',' -f 2,2

  359  ls

  360  cat arch_I.txt arch_II.txt arch_III.txt arch_IV.txt | cut -d ',' -f 2,2

  361  history

