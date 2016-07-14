from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[291.81625,38.135556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19272+3808/sdB_Kepler_J19272+3808_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19272+3808/sdB_Kepler_J19272+3808_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
