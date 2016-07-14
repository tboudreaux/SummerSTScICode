from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.925,26.432717],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FB_179/sdB_FB_179_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FB_179/sdB_FB_179_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
