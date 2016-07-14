from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[67.389167,7.698094],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hz_11/sdB_hz_11_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hz_11/sdB_hz_11_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
