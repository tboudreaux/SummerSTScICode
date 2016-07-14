from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[123.88,24.872944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_081531.20+245222.6/sdB_sdssj9-10_081531.20+245222.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_081531.20+245222.6/sdB_sdssj9-10_081531.20+245222.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
