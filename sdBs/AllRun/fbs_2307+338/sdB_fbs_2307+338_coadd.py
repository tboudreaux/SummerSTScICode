from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[347.557792,34.032833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2307+338/sdB_fbs_2307+338_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2307+338/sdB_fbs_2307+338_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
