from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.851792,36.431389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2237+362/sdB_FBS_2237+362_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2237+362/sdB_FBS_2237+362_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
