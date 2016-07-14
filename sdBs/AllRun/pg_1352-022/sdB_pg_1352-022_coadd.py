from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.769625,-2.506025],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1352-022/sdB_pg_1352-022_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1352-022/sdB_pg_1352-022_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()