from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[152.346042,-14.717525],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1006-145/sdB_PG_1006-145_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1006-145/sdB_PG_1006-145_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
