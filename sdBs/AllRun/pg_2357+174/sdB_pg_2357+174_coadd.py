from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[0.065625,17.648092],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_2357+174/sdB_pg_2357+174_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_2357+174/sdB_pg_2357+174_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
