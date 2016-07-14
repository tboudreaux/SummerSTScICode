from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[194.922833,16.807631],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1257+171/sdB_pg_1257+171_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1257+171/sdB_pg_1257+171_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()