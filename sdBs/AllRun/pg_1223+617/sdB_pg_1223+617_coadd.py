from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[186.480667,61.408097],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1223+617/sdB_pg_1223+617_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1223+617/sdB_pg_1223+617_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
