from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[310.760208,10.572539],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LSIV+10_9/sdB_LSIV+10_9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LSIV+10_9/sdB_LSIV+10_9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
