from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[346.626625,44.313694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2304+440/sdB_FBS_2304+440_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2304+440/sdB_FBS_2304+440_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
