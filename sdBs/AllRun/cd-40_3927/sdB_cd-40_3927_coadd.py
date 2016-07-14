from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.632,-40.546253],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cd-40_3927/sdB_cd-40_3927_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cd-40_3927/sdB_cd-40_3927_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
