from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[18.048542,-26.224381],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FB_15/sdB_FB_15_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FB_15/sdB_FB_15_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
