from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.631458,39.374792],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_07592+3931/sdB_KUV_07592+3931_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_07592+3931/sdB_KUV_07592+3931_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
