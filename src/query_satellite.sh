#!/usr/bin/env bash

for region in "frh01" "frh02" "frh03" "frh04"; do
python PIR-Breizhcrops/src/query_gee.py /data2/france2018/${region}.shp --start 2018-01-01 --end 2018-12-31 --label-col CODE_CULTU --id-col ID_PARCEL --outfolder /data2/france2018/csv/$region
done

# for %x in "frh01" "frh02" "frh03" "frh04" do python C:/Users/Formation/Desktop/PIR_Breizhcrops/processing/query_gee.py C:/Users/Formation/Desktop/PIR_Breizhcrops/data/2019/%x.shp --start 2019-01-01 --end 2019-12-31 --label-col CODE_CULTU --id-col ID_PARCEL --outfolder C:/Users/Formation/Desktop/PIR_Breizhcrops/data/csv/%x.csv

# for region in "frh01" "frh02" "frh03" "frh04"; do python home/Formation/Desktop/PIR_Breizhcrops/processing/query_gee.py /home/lisa_argento/Formation/Desktop/PIR_Breizhcrops/data/2019/{}.shp --start 2019-01-01 --end 2019-12-31 --label-col CODE_CULTU --id-col ID_PARCEL --outfolder C:/Users/Formation/Desktop/PIR_Breizhcrops/data/csv/$region
# done

# python C:/Users/Formation/Desktop/PIR_Breizhcrops/processing/query_gee.py C:/Users/Formation/Desktop/PIR_Breizhcrops/data/2019/frh01.shp --start 2019-01-01 --end 2019-12-31 --label-col CODE_CULTU --id-col ID_PARCEL --outfolder C:/Users/Formation/Desktop/PIR_Breizhcrops/data/csv/frh01.csv
