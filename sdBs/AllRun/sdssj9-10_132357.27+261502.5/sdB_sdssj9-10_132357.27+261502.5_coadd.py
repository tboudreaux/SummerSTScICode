from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[200.988625,26.250694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_132357.27+261502.5/sdB_sdssj9-10_132357.27+261502.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_132357.27+261502.5/sdB_sdssj9-10_132357.27+261502.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
