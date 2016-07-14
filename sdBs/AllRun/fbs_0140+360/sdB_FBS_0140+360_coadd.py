from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[25.926708,36.25925],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0140+360/sdB_FBS_0140+360_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0140+360/sdB_FBS_0140+360_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
