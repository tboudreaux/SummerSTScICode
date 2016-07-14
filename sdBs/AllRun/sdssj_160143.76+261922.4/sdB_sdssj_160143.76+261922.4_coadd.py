from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[240.432333,26.322889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_160143.76+261922.4/sdB_sdssj_160143.76+261922.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_160143.76+261922.4/sdB_sdssj_160143.76+261922.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
