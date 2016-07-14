from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[247.403583,31.403306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_162936.86+312411.9/sdB_sdssj9-10_162936.86+312411.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_162936.86+312411.9/sdB_sdssj9-10_162936.86+312411.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
