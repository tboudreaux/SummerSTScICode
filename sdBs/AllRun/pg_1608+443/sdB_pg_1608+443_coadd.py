from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[242.647042,44.177933],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1608+443/sdB_pg_1608+443_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1608+443/sdB_pg_1608+443_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
