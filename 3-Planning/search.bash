start=1
end=10
for problem in 1 2 3
do 
    for test in 10 #((test=start; test<=end; test++))
    do
        echo -n "Problem $problem test $test"
        python run_search.py -p $problem -s $test >> p${problem}_search.txt
        echo "Done"
    done
    echo -e "p${problem} is done\n"
done
echo "Complete"
