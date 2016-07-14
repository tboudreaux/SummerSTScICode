from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[57.128042,-50.500997],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lb_1695/sdB_lb_1695_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lb_1695/sdB_lb_1695_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
