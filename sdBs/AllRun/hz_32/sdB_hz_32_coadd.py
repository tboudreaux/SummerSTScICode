from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.756542,37.181108],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hz_32/sdB_hz_32_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hz_32/sdB_hz_32_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
