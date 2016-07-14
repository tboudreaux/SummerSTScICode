from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[112.493458,-2.110417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_RWT_152/sdB_RWT_152_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_RWT_152/sdB_RWT_152_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
