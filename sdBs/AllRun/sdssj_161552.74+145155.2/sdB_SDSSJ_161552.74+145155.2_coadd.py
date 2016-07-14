from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.96975,14.865333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_161552.74+145155.2/sdB_SDSSJ_161552.74+145155.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_161552.74+145155.2/sdB_SDSSJ_161552.74+145155.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
