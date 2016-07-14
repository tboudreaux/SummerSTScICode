from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[264.588292,29.146469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bd+29_3070/sdB_bd+29_3070_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bd+29_3070/sdB_bd+29_3070_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
