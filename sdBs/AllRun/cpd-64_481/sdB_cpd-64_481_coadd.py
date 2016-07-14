from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[86.997083,-64.384189],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cpd-64_481/sdB_cpd-64_481_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cpd-64_481/sdB_cpd-64_481_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
