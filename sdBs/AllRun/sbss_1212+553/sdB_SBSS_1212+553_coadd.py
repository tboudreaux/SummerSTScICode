from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[183.604,55.039997],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_1212+553/sdB_SBSS_1212+553_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_1212+553/sdB_SBSS_1212+553_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
