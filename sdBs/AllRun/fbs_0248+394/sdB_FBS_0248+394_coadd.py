from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[42.803875,39.62925],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0248+394/sdB_FBS_0248+394_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0248+394/sdB_FBS_0248+394_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
