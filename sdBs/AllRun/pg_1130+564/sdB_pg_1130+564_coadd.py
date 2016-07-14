from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[173.419292,56.107158],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1130+564/sdB_pg_1130+564_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1130+564/sdB_pg_1130+564_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()