from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[233.29475,5.540778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1530+057/sdB_pg_1530+057_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1530+057/sdB_pg_1530+057_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
