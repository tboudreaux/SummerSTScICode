from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.669625,0.591781],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1136-003/sdB_pg_1136-003_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1136-003/sdB_pg_1136-003_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
