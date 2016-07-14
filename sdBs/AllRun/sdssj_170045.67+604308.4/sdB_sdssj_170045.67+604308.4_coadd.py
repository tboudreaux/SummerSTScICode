from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[255.190292,60.719],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_170045.67+604308.4/sdB_sdssj_170045.67+604308.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_170045.67+604308.4/sdB_sdssj_170045.67+604308.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
