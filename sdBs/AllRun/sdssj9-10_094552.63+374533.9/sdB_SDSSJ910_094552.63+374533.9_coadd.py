from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[146.469292,37.759417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_094552.63+374533.9/sdB_SDSSJ910_094552.63+374533.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_094552.63+374533.9/sdB_SDSSJ910_094552.63+374533.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
