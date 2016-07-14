from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[114.923833,-27.456203],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LSS_630/sdB_LSS_630_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LSS_630/sdB_LSS_630_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
