from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[235.179667,43.997356],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1539+442/sdB_PG_1539+442_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1539+442/sdB_PG_1539+442_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()