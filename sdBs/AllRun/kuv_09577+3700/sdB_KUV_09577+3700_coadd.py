from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[150.172542,36.752278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_09577+3700/sdB_KUV_09577+3700_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_09577+3700/sdB_KUV_09577+3700_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
