from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[259.124667,57.855889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_171629.92+575121.2/sdB_SDSSJ_171629.92+575121.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_171629.92+575121.2/sdB_SDSSJ_171629.92+575121.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()