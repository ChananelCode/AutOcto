reptyr_session=`ps aux|grep "python3 octopus.py fakeit" | grep -v grep | tr -s " " | cut -d " " -f2`
reptyr -s $reptyr_session
