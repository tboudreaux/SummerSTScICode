from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[16.712667,-33.342017],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fb_14/sdB_fb_14_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fb_14/sdB_fb_14_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()