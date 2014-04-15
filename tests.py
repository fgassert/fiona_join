
from fiona_join import *
import fiona


def main():
    joincsvtoshp('multip.shp','OBJECTID','unordered.csv','id','out.shp')
    print "should join 2/3 with 2 warnings"
    print "output:"
    rows = []
    with fiona.open('out.shp') as source:
        for item in source:
            rows.append(item['properties'])
    df = pd.DataFrame(rows)
    print df

if __name__ == "__main__":
   main()
