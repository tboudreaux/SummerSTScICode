from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[332.829083,35.6495],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2209+354/sdB_FBS_2209+354_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2209+354/sdB_FBS_2209+354_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
