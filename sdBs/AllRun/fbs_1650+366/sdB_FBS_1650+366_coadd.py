from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.124375,36.504583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_1650+366/sdB_FBS_1650+366_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_1650+366/sdB_FBS_1650+366_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
