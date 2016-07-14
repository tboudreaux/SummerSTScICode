from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.690005,-33.342017],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FB_14/sdB_FB_14_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FB_14/sdB_FB_14_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
