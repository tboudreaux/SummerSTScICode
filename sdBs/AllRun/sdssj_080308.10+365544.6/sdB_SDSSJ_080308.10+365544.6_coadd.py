from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.78375,36.929056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_080308.10+365544.6/sdB_SDSSJ_080308.10+365544.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_080308.10+365544.6/sdB_SDSSJ_080308.10+365544.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
