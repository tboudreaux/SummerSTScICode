from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[251.547708,27.797889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_164611.45+274752.4/sdB_sdssj9-10_164611.45+274752.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_164611.45+274752.4/sdB_sdssj9-10_164611.45+274752.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
